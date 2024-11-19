/** @odoo-module **/
import { registry } from '@web/core/registry';
import { Component } from '@odoo/owl';
import { _t } from "@web/core/l10n/translation";

export class DoctorDashboard1 extends Component {
    setup() {
        super.setup(...arguments);
    }

    showAlert() {
        // Play sound
        const audio = new Audio('/hospital_customization/static/src/sounds/alert_siound2.mp3');
        audio.play()
            .then(() => {
            })
            .catch(error => {
                console.error("Error playing sound:", error);
            });
        alert(_t("Hello")); 
    }
}

// Assign the template to the component
DoctorDashboard1.template = "DoctorDashboard3";

// Register the component in the actions category
registry.category("actions").add('js_dashboard_tags', DoctorDashboard1);
