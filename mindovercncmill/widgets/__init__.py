from qtpyvcp.widgets.qtdesigner import _DesignerPlugin

from probe_push_button import ProbePushButton
class ProbePushButton_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return ProbePushButton

from probe_wizard_widget import ProbeWizardWidget
class ProbeWizardWidget_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return ProbeWizardWidget

from probe_param_input import ProbeParamInputWidget
class ProbeParamInputWidget_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return ProbeParamInputWidget

from qml_probe.qml_probe import QmlProbe
class QmlProbe_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return QmlProbe

from spindle_widget import SpindleWidget
class SpindleWidget_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return SpindleWidget