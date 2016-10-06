import stripe


stripe.api_key = 'tGN0bIwXnHdwOa85VABjPdSn8nWY7G7I'

print( "Attempting charge..." )

stripe.proxy = {
    "http": "http://<user>:<pass>@<proxy>:<port>",
    "https": "http://<user>:<pass>@<proxy>:<port>" }

clients = ( 
    stripe.http_client.RequestsClient( 
        verify_ssl_certs= stripe.verify_ssl_certs,
        proxy= stripe.proxy )
    ,
    stripe.http_client.PycurlClient( 
        verify_ssl_certs= stripe.verify_ssl_certs,
        proxy= stripe.proxy )
    ,
    stripe.http_client.Urllib2Client( 
        verify_ssl_certs= stripe.verify_ssl_certs,
        proxy= stripe.proxy ) )

for c in clients:
    stripe.default_http_client = c
    resp = stripe.Charge.create(
        amount=200,
        currency='usd',
        card={
            'number': '4242424242424242',
            'exp_month': 10,
            'exp_year': 2019
        },
        description='customer@gmail.com'
    )
    print( 'Success: %s, %r' % ( c.name, resp, ) )
