FROM fsodano79/raspbian:bullseye-20220901

# Install required packages and directories
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3=3.9.2-3 \
        python3-gpiozero=1.4.1-1.3 \
        python3-rpi.gpio=0.7.0-0.2+b1 \
        python3-libcamera=0~git20220826+3fad116f-1 \
        python3-picamera2=0.3.3-1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -y autoremove \
    && mkdir /usr/src/app \
    && mkdir /usr/src/app/birdy_files \
    && mkdir /usr/src/app/birdy_files/images

# Application source
WORKDIR /usr/src/app
ADD . /usr/src/app/

# Install application dependencies
RUN python3 -m pip install -r requirements.txt

# Run the birdy_watcher
CMD ["python3","birdy_watcher.py"]