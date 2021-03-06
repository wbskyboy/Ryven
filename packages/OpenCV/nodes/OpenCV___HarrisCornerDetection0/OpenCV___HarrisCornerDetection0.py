from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node
from custom_src.retain import m


# API METHODS

# self.main_widget        <- access to main widget
# self.update_shape()     <- recomputes the whole shape and content positions

# Ports
# self.input(index)                   <- access to input data
# set_output_val(self, index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_new_input(type_, label, append=True, widget_type='', widget_name='', widget_pos='under', pos=-1)
# self.delete_input(index or input)
# self.create_new_output(type_, label, append=True, pos=-1)
# self.delete_output(index or output)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', 'global')
# self.log_message('that\'s not good', 'error')

# ------------------------------------------------------------------------------

import cv2

class HarrisCornerDetection_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(HarrisCornerDetection_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = self.actionmethod ...
        # ...

        self.initialized()

    # don't call self.update_event() directly, use self.update() instead
    def update_event(self, input_called=-1):
        result = cv2.cornerHarris(self.input(0), self.input(1), self.input(2), self.input(3))
        self.main_widget.show_image(result)
        self.set_output_val(0, result)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass # ...



    # optional - important for threading - stop everything here
    def removing(self):
        pass
