bw = 80;  // base width
bl = 172; // base length
bh = 22;  // base height
wt = 2;   // wall thickness

quick_print = false;
show_addons = false;

use <base_clip.scad>
use <ultrasonic-holder.scad>
use <addon_support.scad>
use <addon_shield.scad>
use <addon_servo.scad>

module base(height=bh) {
    difference() {
        color("gray") cube([bl, bw, height]);
        color("gray") translate([wt, wt, -1]) cube([bl - 2*wt, bw - 2*wt, height+2]);
        
        // hole for power switch
        color("yellow") translate([wt/2, 71, bh/2]) rotate(90, [0, 1, 0]) cylinder(h=2*wt, d=6, center=true, $fn=40);
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
            translate([-7, bw/2, 0]) us_hole(); // back
            translate([bl+7, bw/2, 0]) rotate(180, [0, 0, 1]) us_hole(); // front
            translate([bl/2, -7, 0]) rotate(90, [0, 0, 1]) us_hole();
            translate([bl/2, bw+7, 0]) rotate(-90, [0, 0, 1]) us_hole();
        }
        color("aqua") union() {
            translate([-7, bw/2, 0]) us_holder(); // back
            translate([bl+7, bw/2, 0]) rotate(180, [0, 0, 1]) us_holder(); // front
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
        translate([25, wt, height]) addon_holder();
        translate([100, wt, height]) addon_holder();
        translate([bl-20, wt, height]) addon_holder();
        // outside
        translate([10, 0, height]) mirror([0, 1, 0]) addon_holder();
        translate([55, 0, height]) mirror([0, 1, 0]) addon_holder();
        translate([bl-55, 0, height]) mirror([0, 1, 0]) addon_holder();
        translate([bl-10, 0, height]) mirror([0, 1, 0]) addon_holder();
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
    translate([25, bw/2, bh+wt]) addon_shield();
    translate([bl-20, bw/2, bh+wt]) addon_servo();
}
