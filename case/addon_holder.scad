
module addon_holder() {
    iw = 10; // inner width
    it = 3;  // inner thickness
    h = 5;   // height
    wt = 2;  // wall thickness
    
    module reinforcement() {
        rotate(90, [0, 0, 1])
        rotate(90, [1, 0, 0])
        linear_extrude(height=wt)
        polygon([
            [0, 0],
            [it+wt, 0],
            [0, -h]
        ]);
    }
    
    translate([-wt-iw/2, 0, -h]) {
        difference() {
            cube([iw+2*wt, it+wt, h]);
            translate([wt, -1, -1]) cube([iw, it+1, h+2]);
        }
        reinforcement();
        translate([iw+wt, 0, 0]) reinforcement();
    }
}

addon_holder();
