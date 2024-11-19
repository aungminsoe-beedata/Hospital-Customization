/** @odoo-module **/
import { patch } from "@web/core/utils/patch";
import { ImageField } from "@web/views/fields/image/image_field";

const composerPatch = {
    async onClickCamera(ev) { 
        console.log(ev);
        this.videoElement = ev.target.parentElement.querySelector('#videoCam');
        this.modalElement = $('#myModal');
        
        this.modalElement.modal('show');
        
        try {
            // Request camera access
            const vidStream = await navigator.mediaDevices.getUserMedia({ audio: false, video: true });
            this.vidStream = vidStream;
            this.videoElement.srcObject = vidStream;

            // Play the video stream
            this.videoElement.onloadedmetadata = () => {
                this.videoElement.play();
            console.log('get access')
            console.log('get access---------------------------')
            };
        } catch (e) {
            console.error(e.name + ": " + e.message);
            alert("Unable to access camera. Please check permissions.");
        }
    },
    async ImageCapture(ev) {
        const canvas = ev.target.offsetParent.querySelector('#canvas');
        const video = ev.target.offsetParent.querySelector('#videoCam');
        const context = canvas.getContext('2d');
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
        const image_data_url = canvas.toDataURL('image/jpeg');
        
        const arr = image_data_url.split(','),
              mime = arr[0].match(/:(.*?);/)[1],
              bstr = atob(arr[1]),
              n = bstr.length,
              u8arr = new Uint8Array(n);
        while (n--) {
            u8arr[n] = bstr.charCodeAt(n);
        }
        
        const file = new File([u8arr], 'image.jpeg', { type: mime });
        await this.attachmentUploader.uploadFile(file);
        this.OnClickCancel();
    },
    OnClickCancel() {
        if (this.vidStream) {
            this.vidStream.getTracks().forEach(track => track.stop());
        }
        this.modalElement.modal('hide');
    },
}

patch(ImageField.prototype, composerPatch);
