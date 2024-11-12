t=1.5;
$fn=10;

module base_clip_side() {
    wb=18;
    wt=11;
    h=11;
    
    // clip
    rotate(90, [1, 0, 0])
    translate([-wb, -h, 0])
    linear_extrude(height=t)
    polygon([
        [0, h],
        [wb-wt+t, 0],
        [wb+t, 0],
        [wb+t, h]
    ]);
    
    // hold
    rotate(-90, [0, 0, 1])
    rotate(90, [1, 0, 0])
    linear_extrude(height=wb)
    polygon([
        [0, 0],
        [0, t*2],
        [t, 0]
    ]);
}

module base_clip() {
    hole_x=5.5;
    hole_y=8.8;
    
    difference() {
        union() {
            color("red") base_clip_side();
            color("blue") mirror([1, 0, 0]) rotate(-90, [0, 0, 1]) base_clip_side();
            color("yellow") translate([-hole_x, 0, -hole_y]) sphere(d=t);
        };
         color("red") translate([t, 0, 0]) rotate(-45, [0, 0, 1]) translate([0, -5, -15]) cube([10, 10, 20]);
    }
}

base_clip();