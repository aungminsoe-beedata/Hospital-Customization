/** @odoo-module */
import { registry} from '@web/core/registry';
import { useService } from "@web/core/utils/hooks";
import { useRef } from "@odoo/owl";
import { Component, useState,onWillStart } from "@odoo/owl";
import { _t } from "@web/core/l10n/translation";


// Hospital Dashboard component initialization
export class Hospital_Dashboard extends Component {
    setup() {
       
        this.state = useState({
            courses:[]
        })
       this.ormService = this.env.services.orm;
       onWillStart(async()=>{
        await this.getAllPublishedCourses();
       })
    }
    async getAllPublishedCourses() {
        try {
            this.state.courses = await this.ormService.searchRead(
                'account.move',
                [['ref', 'ilike', 'IMG%']],
                ['id', 'name', 'ref', 'amount_total_signed', 'state']
            );

            // Calculate the sum of amount_total_signed
            const totalAmount = this.state.courses.reduce((sum, course) => sum + course.amount_total_signed, 0);
            console.log('Total Amount:', totalAmount); // Log the sum
        } catch (error) {
            console.error('Error fetching courses:', error);
        }
    }
    
    
}

Hospital_Dashboard.template = "hospital_dashboard_tags"
registry.category("actions").add('hospital_dashboard_tags', Hospital_Dashboard);


