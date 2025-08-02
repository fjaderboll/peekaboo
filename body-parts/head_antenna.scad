use <head_face.scad>
use <addon_support.scad>

module head_antenna_single() {
    translate([25, 5, 54])
    rotate(-35, [0, 1, 0])
    rotate(-90, [0, 0, 1])
    union() {
        addon_clip();
        
        translate([0, 4, 1.6])
        rotate(35, [0, 0, 1])
        rotate(35, [1, 0, 0])
        hull() {
            cylinder(h=2, d=6, $fn=40);
            
            translate([0, 40, 0])
            cylinder(h=1, d=3, $fn=40);
        }
    }
}

module head_antenna() {
    head_antenna_single();
    mirror([1, 0, 0]) head_antenna_single();
}

% color("gray") head_face();
head_antenna();
