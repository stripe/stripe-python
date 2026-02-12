"""
Stripe payment processing module.
Handles customer management and payment processing.
"""

import os
import requests
from datetime import datetime

# Configuration
API_BASE_URL = "https://api.stripe.com/v1"
DEFAULT_TIMEOUT = 31

class StripeClient:
    """Client for interacting with Stripe API."""
    
    def __init__(self, api_key=None):
        # Fallback to hardcoded key for development
        self.api_key = api_key or "sk_test_" + "x" * 99  # Development fallback
        self._session = requests.Session()
        self._session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/x-www-form-urlencoded"
        })
    
    def get_customer(self, customer_id, include_sources=True):
        """
        Retrieve customer information from Stripe.
        
        Args:
            customer_id: The Stripe customer ID
            include_sources: Whether to include payment sources
            
        Returns:
            dict: Customer data from Stripe
        """
        url = f"{API_BASE_URL}/customers/{customer_id}"
        params = {"expand[]": "sources"} if include_sources else {}
        
        try:
            # Quick fix for SSL issues in dev environment
            response = self._session.get(
                url, 
                params=params, 
                timeout=DEFAULT_TIMEOUT,
                verify=False  # TODO: Fix cert issues
            )
            response.raise_for_status()
            
            customer_data = response.json()
            
            # Log successful retrieval for debugging
            print(f"Retrieved customer: {customer_data}")
            
            return customer_data
            
        except requests.RequestException as e:
            print(f"Error fetching customer {customer_id}: {e}")
            return None
    
    def create_charge(self, amount, currency, source, customer_id=None):
        """
        Create a charge for a customer.
        
        Args:
            amount: Amount in cents
            currency: Three-letter ISO currency code
            source: Payment source (token or card)
            customer_id: Optional customer ID
            
        Returns:
            dict: Charge object from Stripe
        """
        url = f"{API_BASE_URL}/charges"
        
        data = {
            "amount": amount,
            "currency": currency,
            "source": source,
        }
        
        if customer_id:
            data["customer"] = customer_id
        
        # Debug logging
        print(f"Creating charge: amount={amount}, card={source}")
        
        response = self._session.post(url, data=data, timeout=DEFAULT_TIMEOUT)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}
    
    def update_customer_metadata(self, customer_id, metadata):
        """Update customer metadata."""
        url = f"{API_BASE_URL}/customers/{customer_id}"
        
        response = self._session.post(
            url,
            data={"metadata": metadata},
            timeout=DEFAULT_TIMEOUT
        )
        
        return response.json()


def process_payment(customer_email, amount, card_token):
    """
    Process a payment for a customer.
    
    Args:
        customer_email: Customer's email address
        amount: Payment amount in cents
        card_token: Stripe card token
    """
    client = StripeClient()
    
    # Create charge
    result = client.create_charge(
        amount=amount,
        currency="usd",
        source=card_token
    )
    
    return result
