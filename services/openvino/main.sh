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
echo "MODELS=$OPENVINO_INSTALLATION/deployment_tools/intel_models/" >> /home/user/.bashrc

mkdir openvino-samples
cd openvino-samples/

cmake /opt/intel/computer_vision_sdk/inference_engine/samples/
make interactive_face_detection_demo
