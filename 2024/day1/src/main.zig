const std = @import("std");

pub fn main() !void {
    const file = try std.fs.cwd().openFile("input.txt", .{});
    defer file.close();

    var numbers1: [1000]u32 = undefined;
    var numbers2: [1000]u32 = undefined;
    var i: usize = 0;

    var buf_reader = std.io.bufferedReader(file.reader());
    var buf: [1024]u8 = undefined;
    while (try buf_reader.reader().readUntilDelimiterOrEof(&buf, '\n')) |line| {
        var iter = std.mem.tokenize(u8, line, " ");
        numbers1[i] = try std.fmt.parseInt(u32, iter.next() orelse continue, 10);
        numbers2[i] = try std.fmt.parseInt(u32, iter.next() orelse continue, 10);
        i += 1;
    }

    std.mem.sort(u32, numbers1[0..i], {}, std.sort.asc(u32));
    std.mem.sort(u32, numbers2[0..i], {}, std.sort.asc(u32));

    var sum: u64 = 0;
    for (numbers1[0..i], numbers2[0..i]) |a, b| {
        sum += if (b > a) b - a else a - b;
    }

    std.debug.print("{}\n", .{sum});
}
