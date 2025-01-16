def lambda_handler(event, context):
    # Extracting numbers from the event
    num1 = event.get('num1')
    num2 = event.get('num2')


    # Adding the numbers
    result = num1 + num2


    # Returning the result
    return {
        'statusCode': 200,
        'body': {
            'result': result
        }
    }