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
