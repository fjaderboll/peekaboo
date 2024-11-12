bw = 80;  // base width
bl = 172; // base length
bh = 22;  // base height
wt = 2.0; // wall thickness

$fn = 50;

use <base_clip.scad>
use <ultrasonic-holder.scad>

module base() {
    difference() {
        cube([bl, bw, bh]);
        translate([wt, wt, -1]) cube([bl - 2*wt, bw - 2*wt, bh+2]);
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

union() {
    difference() {
        color("gray") base();
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
    union() {
        translate([bl, 0, 0]) base_clip();
        translate([bl, bw, 0]) mirror([0, 1, 0]) base_clip();
        translate([0, bw, 0]) mirror([0, 1, 0]) mirror([1, 0, 0]) base_clip();
        translate([0, 0, 0]) mirror([1, 0, 0]) base_clip();
    }
}
