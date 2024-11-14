bw = 80;  // base width
wt = 2;   // wall thickness

sw = 12;  // servo width
sl = 23;  // servo length

hl = 32.8; // servo holder length
ht = 2.5;  // servo holder thickness
cw = 4.8;  // cord width

m = 0.25; // margin

use <addon_support.scad>

module addon_bar_servo() {
    w = bw-2*wt;
    
    difference() {
        union() {
            addon_bar(w);
            color("orange") translate([0, w/2, wt/2-ht/2]) cube([sw+2*m+2*wt, hl+2*m+2*wt, wt+ht], center=true);
        }
    
        // top large hole
        color("orange") translate([0, w/2, wt]) cube([sw+2*m, hl+2*m, 2*ht], center=true);
        // bottom smaller hole
        color("orange") translate([0, w/2, -wt]) cube([sw+2*m, sl+2*m, 2*wt], center=true);
        // cord hole
        color("orange") translate([0, w/2, -wt]) cube([cw+2*m, hl+2*m, 2*wt], center=true);
    }
}

addon_bar_servo();
