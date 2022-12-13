#--------------------------------------------------
# mau_blendCam.py
# version: 0.0.1
# last updated: 15.05.22 (DD.MM.YY)
#--------------------------------------------------


# Import the required modules
import nuke

# Get the selected node
node = nuke.selectedNode()

# Get the list of all layers in the Read node
channels = node.channels()
layers = list( set([c.split('.')[0] for c in channels]) )

# Create a shuffle node for each layer
for layer in layers:
  shuffle = nuke.nodes.Shuffle()
  shuffle.setInput(0, read_node)
  shuffle.knob("name").setValue(format(layer))
  shuffle["in"].setValue(layer)
