/** @odoo-module **/

import { ImageField } from '@web/views/fields/image/image_field';
import { patch } from "@web/core/utils/patch";
import { CameraDialog } from "./CameraDialog.js";
import { useService } from "@web/core/utils/hooks";
 /**
 * Updates ImageField
 */
patch(ImageField.prototype,{
    setup(){
        super.setup();
        this.dialogService = useService('dialog')
    },
    onFileCamera(ev){
        ev.stopPropagation()
        this.dialogService.add(CameraDialog, {parent: this},);
    }
})

/***
 * The((  ImageField )) component is a part of Odoo's modern JavaScript framework (OWL).
 *  It provides the interface for displaying an image, and interacting with it 
 * (e.g., uploading a new image, removing an image, etc.). When patching the ImageField widget,
 *  as in the code you shared, you're adding or overriding functionality related to how the image 
 * field behaves in your custom module.
 */
