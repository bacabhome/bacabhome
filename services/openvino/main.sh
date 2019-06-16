#!/bin/bash

# =============================================================================
# Variables
# =============================================================================

OPENVINO_INSTALLATION=/opt/intel/openvino/

# =============================================================================
# Functions
# =============================================================================

# None

# =============================================================================
# Main
# =============================================================================

cd $HOME

echo "MODELS=$OPENVINO_INSTALLATION/deployment_tools/intel_models/" >> /home/user/.bashrc

mkdir openvino-samples
cd openvino-samples/

# Samples

cmake /opt/intel/computer_vision_sdk/inference_engine/samples/
make all
