bw = 80;   // base width
wt = 2;    // wall thickness

m = 0.30;  // margin
pt = 1.5;  // PCB thickness
ht = 1.0;  // holder thickness

sw = 64.4; // shield width
sh = 53.5; // shield height
aw = 20;   // addon card width
ah = 80;   // addon card height

use <addon_support.scad>

module addon_shield() {
    w = bw-2*wt;
    
    module clips_oneside() {
        translate([0, -w/2, -wt]) addon_bar(width=15, single_clip=true);
        translate([75, -w/2, -wt]) addon_bar(width=15, single_clip=true);
        color("orange") translate([-9.5, -w/2+10, 1-wt]) rotate(90, [0, 1, 0], $fn=40) cylinder(h=90.5, d=5);
    }
    module clips() {
        clips_oneside();
        mirror([0, 1, 0]) clips_oneside();
    }
    module cards_holder() {
        tw = wt+sw+wt+aw+wt+4*m;
        tt = ht+pt+ht+2*m;
        th = wt+sh+m;
        
        difference() {
            // full size
            translate([0, -tt/2, 0]) cube([tw, tt, th]);
            // shield hole
            x1=wt;
            translate([x1, -(pt+2*m)/2, wt]) cube([sw+2*m, pt+2*m, th]);
            // see-through shield hole
            translate([x1+ht, -tt, wt+ht]) cube([sw+2*m-2*ht, 2*tt, th]);
            translate([x1+ht+2, -(pt+m)/2-tt, -wt]) cube([sw+2*m-2*ht-5-3, tt, th]);
            
            // addon card hole
            x2=x1+wt+sw+3*m;
            translate([x2, -(pt+2*m)/2, wt]) cube([aw+2*m, pt+2*m, th]);
            // see-through addon card hole
            translate([x2+ht, -tt, wt+ht]) cube([aw+2*m-2*ht, 2*tt, th]);
        }
    }
    module foot() {
        s=26;
        translate([0, -28, -1])
        rotate(90, [0, 0, 1])
        rotate(90, [1, 0, 0])
        linear_extrude(height=wt)
        polygon([
            [0, 2.5],
            [s, -17.5],
            [s, -22.5],
            [0, -1]
        ]);
    }
    module triangle() {
        s=29;
        translate([0, -30.5, -1])
        rotate(90, [0, 0, 1])
        rotate(90, [1, 0, 0])
        linear_extrude(height=wt)
        polygon([
            [0, 0],
            [s, s/1.5],
            [s, -s/1.5]
        ]);
    }
    /*module triangle_light() {
        difference() {
            triangle();
            translate([-0.1, 0, 0]) scale([1.1, 0.7, 0.7]) triangle();
        }
    }*/
    module cards_holder_holder() {
        translate([-9.5, 0, 0]) foot();
        translate([57, 0, 0]) triangle();
        translate([79, 0, 0]) triangle();
        
        translate([-9.5, 0, 0]) mirror([0, 1, 0]) triangle();
        translate([57, 0, 0]) mirror([0, 1, 0]) triangle();
        translate([79, 0, 0]) mirror([0, 1, 0]) triangle();
    }
    
    clips();
    color("orange") translate([-10, 0, -22-wt]) cards_holder();
    color("orange") cards_holder_holder();
}

addon_shield();
