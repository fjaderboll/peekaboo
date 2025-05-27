use <addon_support.scad>

bw = 80;  // base width
wt = 2;   // wall thickness

usw = 48; // ultrasonic width

m = 0.20; // margin

plate_points = [
    [0, 5],
    [0, bw/2+5],
    [60, bw/2+5],
    [62, bw/2],
    [70, bw/2-16],
    [70, bw/2-16-usw/2+4],
    [74, bw/2-16-usw/2],
    [40, bw/2-16-usw/2],
    [40, bw/2-16-usw/2+5],
];

module cover_front() {
    module oneside() {
        // clips
        translate([172-10, bw/2, 0]) addon_clip();
        translate([172-55, bw/2, 0]) addon_clip();
        
        difference() {
            // plate
            translate([172-55-5-wt+m, 0, 0])
            linear_extrude(wt)
            polygon(plate_points);
        
            // hole
            translate([142, 0, -wt*0.5])
            cube([20, 39, wt*2]);
        }
    }

    // both sides
    #oneside();
    mirror([0, 1, 0]) oneside();
}

cover_front();
