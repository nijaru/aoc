const std = @import("std");

pub fn main() !void {
    const file = try std.fs.cwd().openFile("input.txt", .{});
    defer file.close();

    var numbers1: [1000]u32 = undefined;
    var numbers2: [1000]u32 = undefined;
    var index: usize = 0;

    var buf_reader = std.io.bufferedReader(file.reader());
    var reader = buf_reader.reader();
    var buf: [1024]u8 = undefined;

    while (try reader.readUntilDelimiterOrEof(&buf, '\n')) |line| {
        const trimmed = std.mem.trim(u8, line, &std.ascii.whitespace);
        if (trimmed.len == 0) continue;

        var tokens = std.mem.tokenizeAny(u8, trimmed, " \t");
        numbers1[index] = try std.fmt.parseInt(u32, tokens.next() orelse continue, 10);
        numbers2[index] = try std.fmt.parseInt(u32, tokens.next() orelse continue, 10);
        index += 1;
    }

    std.mem.sort(u32, &numbers1, {}, std.sort.asc(u32));
    std.mem.sort(u32, &numbers2, {}, std.sort.asc(u32));

    var sum: u64 = 0;
    for (numbers1, numbers2) |a, b| {
        sum += if (b > a) b - a else a - b;
    }

    std.debug.print("{}\n", .{sum});
}
