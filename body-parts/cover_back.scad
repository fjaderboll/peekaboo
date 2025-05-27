use <addon_support.scad>

bw = 80;  // base width
wt = 2;   // wall thickness

usw = 48; // ultrasonic width
ust = 8;  // ultrasonic thickness

cl = 110; // cover length
cx = cl * 0.6;

m = 0.20; // margin

s1 = [1, 0.8];
s2 = [0.5, 0.5];
s3 = [0, 0];

function get_wall_points_outer(gap) = [
        [-ust-4, 0],
        [-ust, 4],
        [-ust, usw/2],
        [0, bw/2+wt],
        [50, bw/2+wt],
        [62, bw/2+wt+ust-2],

        [82, bw/2+wt+ust-2],
        [86, bw/2+wt+ust+2],
        [90, bw/2+wt+ust-2],

        [cl, bw/2+wt+ust-2],
        [cl, gap]
];
function get_wall_points_inner(gap) = [
        [cl-wt, gap],
        [cl-wt, bw/2+ust-2],
        [62, bw/2+ust-2],
        [50, bw/2],
        [1, bw/2],
        [-ust+wt, usw/2],
        [-ust+wt, 0]
];

wall_points_both = concat(get_wall_points_outer(5), get_wall_points_inner(5));
wall_points_closed = get_wall_points_outer(0);

module cover_back() {
    module oneside() {
        // clips
        translate([10, bw/2, 0]) addon_clip();
        translate([55, bw/2, 0]) addon_clip();
        
        // sides
        color("pink")
        linear_extrude(35, scale=s1)
        polygon(wall_points_both);
        
        color("blue")
        translate([0, 0, 35])
        translate([cx, 0, 0])
        linear_extrude(20, scale=s2)
        scale(s1)
        translate([-cx, 0, 0])
        polygon(wall_points_both);
        
        color("orange")
        translate([0, 0, 55-wt])
        translate([cx, 0, 0])
        linear_extrude(wt)
        scale(s2)
        scale(s1)
        translate([-cx, 0, 0])
        polygon(wall_points_closed);
    }

    // both sides
    #oneside();
    mirror([0, 1, 0]) oneside();
}

cover_back();
