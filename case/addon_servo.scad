bw = 80;  // base width
wt = 2;   // wall thickness

sw = 12;  // servo width
sl = 23;  // servo length

hl = 32.8; // servo holder length
ht = 2.5;  // servo holder thickness
cw = 4.8;  // cord width
co = 10;   // cord offset from holder

m = 0.20; // margin

use <addon_support.scad>

module addon_servo() {
    w = bw-2*wt;
    
    difference() {
        union() {
            // bar
            translate([0, -w/2, -wt]) addon_bar(w);
            // holder
            color("orange") translate([0, 0, -(ht+co)/2]) cube([sw+2*m+2*wt, hl+2*m+2*wt, ht+co], center=true);
        }
    
        color("orange")  {
            // top hole for holder
            translate([0, 0, 0]) cube([sw+2*m, hl+2*m, 2*ht], center=true);
            // bottom hole for body
            translate([0, 0, -co]) cube([sw+2*m, sl+2*m, 2*co], center=true);
            // cord hole
            translate([0, 0, -co]) cube([cw+2*m, hl+2*m, 2*co], center=true);
        }
    }
}

addon_servo();
