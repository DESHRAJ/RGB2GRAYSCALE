import cv2
import cvfy
​
app = cvfy.register('')
​
@cvfy.crossdomain
@app.listen()
def grayscale():

    all_image_paths = cvfy.getImageArray() 
    
    image_1_path = all_image_paths[0]
        
    cvfy.sendTextArrayToTerminal(['Loading Image...']);
    image_1 = cv2.imread(image_1_path)

    cvfy.sendTextArrayToTerminal(['Image Loaded successfully']);

    gray_image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)

    cvfy.sendTextArrayToTerminal(['Converting RGB Image to Grayscale']);

    cvfy.sendImageArray([gray_image_1], mode = 'numpy_array')

    cvfy.sendTextArrayToTerminal([
        'Operation completed successfully',
        image_1_path
        ]);

    return 'OK'

app.run()
