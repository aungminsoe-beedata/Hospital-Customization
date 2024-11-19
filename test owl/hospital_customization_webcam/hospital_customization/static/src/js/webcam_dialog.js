/** @odoo-module */
const { Component, useRef, onMounted } = owl;
import { Dialog } from "@web/core/dialog/dialog";
import { session } from '@web/session';

class WebcamDialog extends Component {
    async setup() {
        super.setup();
        this.video = useRef("video");
        onMounted(() => this._startVideo());
    }
    async handleStream(stream) {
        const def = $.Deferred();
        this.video.el.srcObject = stream;
        return def
    }
    async _startVideo() {
        try {
            const videoStream = await navigator.mediaDevices.getUserMedia({
                video:{
                width: { ideal: session.am_webcam_width || 1280 },
                height: { ideal: session.am_webcam_height || 720 },
                }
            })
            await this.handleStream(videoStream)
        } catch (e) {
            console.error('*** getUserMedia', e)
        } finally {
        }
    }
}
WebcamDialog.components = {
    Dialog,
};
WebcamDialog.template = 'hospital_customization.WebcamDialog'
export default WebcamDialog;