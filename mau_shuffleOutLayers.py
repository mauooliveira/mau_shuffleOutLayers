#--------------------------------------------------
# mau_blendCam.py
# version: 0.0.1
# last updated: 13.12.22 (DD.MM.YY)
#--------------------------------------------------

# Import the required modules
import nuke

# Get the selected node
node = nuke.selectedNode()
dot = nuke.createNode('Dot')

# Get the list of all layers in the Read node
channels = node.channels()
layers = list( set([c.split('.')[0] for c in channels]))
if "rgba" in layers:
    layers.remove("rgba")
else:
    pass

# Create a shuffle node for each layer
for layer in layers:
  shuffle = nuke.nodes.Shuffle()
  shuffle.setInput(0, dot)
  shuffle.knob("label").setValue(format(layer))
  shuffle["in"].setValue(layer)
