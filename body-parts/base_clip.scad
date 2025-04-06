
module base_clip() {
    module base_clip_side(width=18) {
        wb=width;
        wt=10;
        h=11;
        t=1.5;
        
        // clip
        rotate(90, [1, 0, 0])
        translate([-wb, -h, 0])
        linear_extrude(height=t)
        polygon([
            [0, h],
            [wb-wt, 0],
            [wb, 0],
            [wb, h]
        ]);
        
        // top
        rotate(-90, [0, 0, 1])
        rotate(90, [1, 0, 0])
        linear_extrude(height=wb)
        polygon([
            [0, 0],
            [0, t*2],
            [t, 0]
        ]);
        
        // corner
        rotate(-45, [0, 0, 1])
        rotate_extrude(angle=-45, $fn=40)
        polygon([
            [0, t*2],
            [t, 0],
            [t, -h],
            [0, -h]
        ]);
    }

    hole_x=5.5;
    hole_y=8.8;
    
    union() {
        color("red") base_clip_side();
        color("blue") mirror([1, 0, 0]) rotate(-90, [0, 0, 1]) base_clip_side(16);
        color("yellow") translate([-hole_x, 0, -hole_y]) sphere(d=1.5, $fn=20);
    };
}

base_clip();