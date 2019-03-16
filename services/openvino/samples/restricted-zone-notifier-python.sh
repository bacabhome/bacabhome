#!/bin/bash

# =============================================================================
# Variables
# =============================================================================

OPENVINO_INSTALLATION=/opt/intel/computer_vision_sdk/

# =============================================================================
# Functions
# =============================================================================

# None

# =============================================================================
# Main
# =============================================================================

cd $HOME

source $OPENVINO_INSTALLATION/bin/setupvars.sh

python3 main.py \
        -ci "${CAMERA_IDENTIFICATION}" \
        -fr 15 \
        -fc XVID \
        -hi ${SINK_HOST_IP} \
        -hp ${SINK_HOST_PORT} \
        -i ${VIDEO_CAPTURE} \
        -m /opt/intel/computer_vision_sdk/deployment_tools/intel_models/person-detection-retail-0013/FP32/person-detection-retail-0013.xml \
        -l /opt/intel/computer_vision_sdk/inference_engine/lib/ubuntu_16.04/intel64/libcpu_extension_sse4.so \
        -d CPU
