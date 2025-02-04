# ai_image_classifier
Upload image and have AI model describe the image. Basic app with no CSS yet.

## To deploy Docker container and host app locally
1) Build the image
```
docker build -t image-classifier-app .
```
2) Run the container
```
docker run -p 5001:5000 image-classifier-app
```
3) Go to browser and enter local address
```
http://127.0.0.1:5000/
```

## Example Output
* Upload image as shown below
[image to analyze](ai_image_classifier/images/ford_lightning_still.png)

* Once image is uploaded and analyzed the output will result:
```
Predictions:
pickup (0.41%), minivan (0.14%), car_wheel (0.09%)
```
* The ratio shown above represents the confidence of the model. 41% confident that it is a pickup. This 
