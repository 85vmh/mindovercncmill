import QtQuick 2.7
import QtQuick.Controls 1.5
import QtQuick.Layouts 1.3

Rectangle {
    id: rectangle
    visible: true
    width: 550
    height: 550
    color: "#939695"
    opacity: 1


    Rectangle {
        id: x_clearance_line
        x: 62
        y: 238
        width: 197
        height: 30

        Image {
            id: image_arrow_right
            x: 179
            y: 0
            width: 18
            height: 30
            fillMode: Image.PreserveAspectFit
            source: "images/arrow-right.png"
        }

        Image {
            id: image_arrow_left
            width: 18
            height: 30
            fillMode: Image.PreserveAspectFit
            source: "images/arrow-left.png"
        }

        Repeater {
            id: x_clearance_slash
            x: image_arrow_left.width
            y: 0
            width: parent.width - (image_arrow_left.width + image_arrow_right.width)
            height: 30
            model: 15
            rotation: 0

            delegate: Item {

                id: x_clearance_slash_item
                height: 64
                width: 100

                Rectangle {
                    id: x_clearance_slash_rectangle
                    x: 12 * (index+1)
                    y:13
                    width: 3
                    height: 3
                    color: "#000000"
                }

            }
        }
    }

    Rectangle {
        id: z_retract_line
        x: 36
        y: 190
        width: 30
        height: 197

        Image {
            id: image_arrow_up
            width: 30
            height: 18
            fillMode: Image.PreserveAspectFit
            source: "images/arrow-up.png"
        }

        Image {
            id: image_arrow_down
            width: 30
            height: 18
            y: 176
            fillMode: Image.PreserveAspectFit
            source: "images/arrow-down.png"
        }

        Repeater {
            id: z_retract_slash
            x: image_arrow_up.height
            y: 0
            width: parent.width - (image_arrow_left.width + image_arrow_right.width)
            height: 30
            model: 15
            rotation: 0

            delegate: Item {

                id: z_retract_slash_item
                height: 64
                width: 100

                Rectangle {
                    id: z_retract_slash_rectangle
                    x: 12
                    y:12 * (index+1)
                    width: 3
                    height: 3
                    color: "#000000"
                }
            }
        }
    }

    Rectangle {
        id: probe
        x: 265
        y: 123 + z_retract
        width: 24
        height: 157
        color: "#00000000"


        Rectangle{
            x:10
            y:0
            width: 4
            height: 143

        }

        Rectangle{
            radius: 8
            x:4
            y:141
            width: 16
            height: 16
            color: "#ca60ff"

        }

    }

    Rectangle {
        id: stock
        x: 160
        y: 304
        width: 202
        height: 77

    }

    // probe Properties

    property int x_clearance: 10;
    property int z_retract: 10;


    Connections {
        target: qml_probe; // the connection betwen python signals

        onXClearanceSig: {
            x_clearance = x_value;
        }

        onZRetractSig: {
            z_retract = z_value;
        }
    }
}

/*##^## Designer {
    D{i:3;anchors_height:16;anchors_width:16;anchors_x:16;anchors_y:149}D{i:13;anchors_height:16;anchors_width:16;anchors_x:16;anchors_y:149}
}
 ##^##*/
