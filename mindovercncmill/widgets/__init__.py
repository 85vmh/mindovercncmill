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

from smart_dro_widget import SmartDro
class SmartDro_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return SmartDro

from notification_status_button import NotificationStatusButton
class NotificationStatusButton_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return NotificationStatusButton

from pause_resume_button import PauseResumeButton
class PauseResumeButton_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return PauseResumeButton