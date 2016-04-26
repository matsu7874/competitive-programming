function Main(input) {
    var rows = input.split("\n");
    var r, c, elms, sy, sx, gy, gx;

    elms = rows[0].split(" ");
    r = parseInt(elms[0], 10);
    c = parseInt(elms[1], 10);

    elms = rows[1].split(" ");
    sy = parseInt(elms[0], 10) - 1;
    sx = parseInt(elms[1], 10) - 1;

    elms = rows[2].split(" ");
    gy = parseInt(elms[0], 10) - 1;
    gx = parseInt(elms[1], 10) - 1;

    var maze = rows.slice(3);
    var queue = [
        [0, sy, sx]
    ];
    var ds = [0, 1, 0, -1, 0];
    var visited = new Array(r);
    for (var i = 0; i < r; ++i) {
        visited[i] = new Array(c);
        for (var j = 0; j < c; ++j) {
            visited[i][j] = false;
        }
    }
    while (queue) {
        q = queue.shift();
        if (q[1] == gy && q[2] == gx) {
            console.log("%d", q[0]);
            return;
        }
        for (var i = 0; i < ds.length - 1; ++i) {
            var dy = ds[i];
            var dx = ds[i + 1];
            if (maze[q[1] + dy][q[2] + dx] == "." && (visited[q[1] + dy][q[2] + dx] == false)) {
                queue.push([q[0] + 1, q[1] + dy, q[2] + dx]);
                visited[q[1] + dy][q[2] + dx] = true;
            }
        }
    }
}

Main(require("fs").readFileSync("/dev/stdin", "utf8"));
