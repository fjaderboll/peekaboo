bw = 80;  // base width
bl = 172; // base length
bh = 22;  // base height
wt = 2;   // wall thickness

quick_print = false;
show_addons = true;

use <base_clip.scad>
use <ultrasonic-holder.scad>
use <addon_support.scad>
use <addon_bar_servo.scad>

module base(height=bh) {
    color("gray") difference() {
        cube([bl, bw, height]);
        translate([wt, wt, -1]) cube([bl - 2*wt, bw - 2*wt, height+2]);
    }
    /*translate([-wt, -wt, -2]) {
        difference() {
            cube([bl+2*wt, bw+2*wt, 5]);
            translate([wt, wt, -1]) {
                cube([bl, bw, 7]);
            }
        }
    }*/
}

module base_with_holders() {
    union() {
        difference() {
            base();
            translate([wt, bw/2, 0]) us_hole();
            translate([bl-wt, bw/2, 0]) rotate(180, [0, 0, 1]) us_hole();
            translate([bl/2, -7, 0]) rotate(90, [0, 0, 1]) us_hole();
            translate([bl/2, bw+7, 0]) rotate(-90, [0, 0, 1]) us_hole();
        }
        color("aqua") union() {
            translate([wt, bw/2, 0]) us_holder();
            translate([bl-wt, bw/2, 0]) rotate(180, [0, 0, 1]) us_holder();
            translate([bl/2, -7, 0]) rotate(90, [0, 0, 1]) us_holder();
            translate([bl/2, bw+7, 0]) rotate(-90, [0, 0, 1]) us_holder();
        }
        
    }
}

module base_clips() {
    union() {
        translate([bl, 0, 0]) base_clip();
        translate([bl, bw, 0]) mirror([0, 1, 0]) base_clip();
        translate([0, bw, 0]) mirror([0, 1, 0]) mirror([1, 0, 0]) base_clip();
        translate([0, 0, 0]) mirror([1, 0, 0]) base_clip();
    }
}

module base_addon_holders(height=bh) {
    module side() {
        // inside
        translate([30, wt, height]) addon_holder();
        translate([60, wt, height]) addon_holder();
        translate([bl-30, wt, height]) addon_holder();
        // outside
        translate([30, 0, height]) mirror([0, 1, 0]) addon_holder();
        translate([bl-30, 0, height]) mirror([0, 1, 0]) addon_holder();
    }
    color("yellow") {
        side();
        translate([0, bw, 0]) mirror([0, 1, 0]) side();
    }
}

if(quick_print) {
    base(height=10);
    base_addon_holders(height=10);
} else {
    base_with_holders();
    base_addon_holders();
}
base_clips();

if(show_addons) {
    translate([bl-30, wt, bh]) addon_bar_servo();
}
