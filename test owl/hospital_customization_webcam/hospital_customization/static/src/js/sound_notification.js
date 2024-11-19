/** @odoo-module **/

import { NotificationService } from '@web/core/notifications/notification_service';
import { patch } from '@web/core/utils/patch';

// Patch the NotificationService to show an alert for danger notifications
patch(NotificationService.prototype, 'hospital_customization.notification_patch', {
    add(message, options) {
        // Call the original add method
        this._super(...arguments);

        // Check if the notification type is 'danger'
        if (options && options.type === 'danger') {
            alert("Hello"); // Show the alert message
        }

        // Optional logging for debugging
        console.log("Notification: ", message, options);
    },
});
