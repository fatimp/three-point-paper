module Shit
import CorrelationFunctions.Directional as D
import CorrelationFunctions.Utilities as U
using NPZ
export draw_ball, do_all!

function draw_ball(s, r)
    array = zeros(Bool, s)
    center = @. (s ÷ 2) |> floor |> Int

    for idx in CartesianIndices(array)
        dist = sum((Tuple(idx) .- center) .^ 2)
        if dist <= r^2
            array[idx]	= true
        end
    end

    return array
end

function do_all!()
    ball = draw_ball((250, 250, 250), 0.2*250)
    println(U.lowfreq_energy_ratio(ball))
    ssv = D.surf2void(ball, false; periodic = true)
    calc = ssv[D.PlaneXY()][end-15, :] * 250^2
    npzwrite("ball-ss.npy", calc)

    svv = D.surfvoid2(ball, false; periodic = true)
    calc = svv[D.PlaneXY()][end-15, :] * 250
    npzwrite("ball-sv.npy", calc)
end

end
