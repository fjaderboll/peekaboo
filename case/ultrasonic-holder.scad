usw=46;
ush=21;
ust=7;
wt=1;

module us_box() {
    color("aqua") translate([-wt, -usw/2-wt, 0]) {
        cube([ust+2*wt, usw+2*wt, ush+wt]);
    }
    
    s=(25.5-17)/2;
    color("aqua")
    translate([-wt, 0, 0])
    linear_extrude(height=ush+wt)
    polygon([
        [0, s],
        [0, -s],
        [-s, 0]
    ]);
}

module us_hole() {
    d=17;
    t=10;
    dx=25.5;
    $fn=50;
    
    // front holes
    color("yellow") translate([-t/2, -dx/2, d/2+2]) {
        union() {
            rotate(90, [0, 1, 0]) cylinder(h=t, r=d/2);
            translate([0, -d/2, 0]) cube([t, d, d]);
        }
        translate([0, dx, 0]) union() {
            rotate(90, [0, 1, 0]) cylinder(h=t, r=d/2);
            translate([0, -d/2, 0]) cube([t, d, d]);
        }
        
    }
    // back hole
    color("yellow") translate([ust-wt/2, -6, wt+ush-4]) cube([wt*2+2, 12, 4.1]);
    
    // inside holes
    color("red") translate([ust/2, -usw/2, wt]) cube([ust/2, usw, ush+0.1]);
    color("green") translate([0, -usw/2+wt, wt]) cube([ust/2+0.1, usw-2*wt, ush+0.1]);
}

module us_holder() {
    difference() {
        us_box();
        us_hole();
    }
}

us_holder();
