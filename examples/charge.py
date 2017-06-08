import stripe

stripe.api_key = 'tGN0bIwXnHdwOa85VABjPdSn8nWY7G7I'

print "Attempting charge..."

resp = stripe.Charge.create(
    amount=200,
    currency='usd',
    card='tok_visa',
    description='customer@gmail.com'
)

print 'Success: %r' % (resp, )
