use <addon_support.scad>

bw = 80;  // base width
wt = 2;   // wall thickness

sw = 12;  // servo width
sl = 23;  // servo length

hl = 32.8; // servo holder length
ht = 2.5;  // servo holder thickness
cw = 4.8;  // cord width
co = 10;   // cord offset from holder

m = 0.20; // margin

module servo_box() {
    color("orange") translate([0, 0, -(ht+co)/2]) cube([sw+2*m+2*wt, hl+2*m+2*wt, ht+co], center=true);
}

module servo_holder() {
    difference() {
        servo_box();
    
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

module addon_servo() {
    w = bw-2*wt;
    
    difference() {
        translate([0, -w/2, -wt]) addon_bar(w);
        translate([0, 0, 0.1]) servo_box();
    }
    servo_holder();
}

addon_servo();
