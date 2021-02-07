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

from gm_codes_table import GMCodesTable
class GMCodesTable_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return GMCodesTable

from wcs_offsets_table import WcsOffsetsTable
class WcsOffsetsTable_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return WcsOffsetsTable

from notifications_widget import NotificationsWidget
class NotificationsWidget_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return NotificationsWidget

from settings_label import SettingsLabel
class SettingsLabelWidget_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return SettingsLabel

from blink_button import BlinkButton
class BlinkButton_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return BlinkButton

from conversational.conversational import ConversationalWizardWidget
class ConversationalWidget_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return ConversationalWizardWidget

from conversational.general_params import GeneralParamsWidget
class GeneralParamsWidget_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return GeneralParamsWidget

from conversational.program_header import ProgramHeaderWidget
class ProgramHeaderWidget_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return ProgramHeaderWidget

from conversational.facing import FacingOpWidget
class FacingOpWidget_Plugin(_DesignerPlugin):
    def pluginClass(self):
        return FacingOpWidget