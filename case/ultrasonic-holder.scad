
module us_hole() {
    d=17;
    t=10;
    dx=25.5;
    
    translate([-t/2, -dx/2, d/2+2]) {
        union() {
            rotate(90, [0, 1, 0]) cylinder(h=t, r=d/2);
            translate([0, -d/2, 0]) cube([t, d, d]);
        }
        translate([0, dx, 0]) union() {
            rotate(90, [0, 1, 0]) cylinder(h=t, r=d/2);
            translate([0, -d/2, 0]) cube([t, d, d]);
        }
    }
}

module us_holder() {
    usw=46;
    ush=22;
    ust=3.5;
    wt=1;
    
    color("aqua") translate([0, -usw/2-wt, 0]) {
        // floor
        cube([7+wt, usw+2*wt, wt]);
        
        // inner sides
        translate([0, wt, 0]) cube([ust, wt, ush]);
        translate([0, usw, 0]) cube([ust, wt, ush]);
        
        // outer sides
        translate([0, 0, 0]) cube([7, wt, ush]);
        translate([0, usw+wt, 0]) cube([7, wt, ush]);
        
        // backside
        difference() {
            translate([7, 0, 0]) cube([wt, usw+2*wt, ush]);
            translate([7-wt/2, usw/2-6+wt, ush-4]) cube([wt*2, 12, 4.1]);
        }
    }
}

union() {
    us_holder();
    difference() {
        color("yellow") translate([-1, -24, 0]) cube([1, 48, 22]);
        us_hole();
    }
}

