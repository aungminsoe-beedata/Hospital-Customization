/** @odoo-module **/

import { ImageField } from "@web/views/fields/image/image_field";
import { useService } from "@web/core/utils/hooks";
import { patch } from "@web/core/utils/patch";
import WebcamDialog from '@hospital_customization/js/webcam_dialog';

patch(ImageField.prototype, {
    setup() {
        this._super(...arguments);
        this.dialogService = useService("dialog");
    },

    _openRearCamera(ev) {
        alert("hello open rear camera")
    },
});
