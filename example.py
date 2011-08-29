import stripe

stripe.api_key = '26OjYWkUnwDegILl9ZNVbefRjRboRSio'

print "Attempting charge..."

resp = stripe.Charge.create(
         amount=200,
         currency='usd',
         card={
           'number': '4242424242424242',
           'exp_month': 10,
           'exp_year': 2014
         },
         description='customer@gmail.com'
       )

print 'Success: %r' % (resp, )
