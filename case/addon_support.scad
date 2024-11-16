iw = 10;  // inner width
it = 3;   // inner thickness
h = 5;    // height
wt = 2;   // wall thickness
m = 0.30; // margin

module addon_holder() {
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
    
    color("yellow") translate([-wt-iw/2, 0, -h]) {
        difference() {
            cube([iw+2*wt, it+wt, h]);
            translate([wt, -1, -1]) cube([iw, it+1, h+2]);
        }
        reinforcement();
        translate([iw+wt, 0, 0]) reinforcement();
    }
}

module addon_clip(bar_length=0) {
    ch = 1.5*h;
    
    color("#fcc705") {
        translate([-(iw-2*m)/2, m, -ch])
        cube([iw-2*m, it-2*m, ch]);
        
        translate([-(iw-2*m)/2, m, 0])
        cube([iw-2*m, it+wt-m, wt]);
    
        translate([0, (it-2*m)/2+m, -ch-1])
        resize([iw-2*m, it-2*m, 1])
        rotate(45, [0, 0, 1])
        cylinder(h=1, r1=it/3, r2=it/2, $fn=4);
    }
}

module addon_bar(width, single_clip=false) {
    addon_clip();
    if(!single_clip) {
        translate([0, width, 0]) mirror([0, 1, 0]) addon_clip();
    }
    
    color("orange")
    translate([-(iw-2*m)/2, it+wt, 0])
    cube([iw-2*m, width-2*(it+wt), wt]);
}

addon_holder();
//addon_bar(width=15, single_clip=true);
addon_bar(width=20);