module Shit
import CorrelationFunctions.Directional as D
import CorrelationFunctions.Utilities as U
using FileIO
using Images
using NPZ

#const sides = 100:200:1200
#const fns = [D.s3, D.c3]

const sides = 700:200:1200
const fns = [D.surf3]

function foo!()
    for side in sides
        for s in 1:9
            datajulia = load("julia-lin/data-$(s)-$(side).tga") .|> Gray .|> Float64 .|> round
            datalisp = load("lisp/data-$(s)-$(side).tga")  .|> Gray .|> Float64

            for fn in fns
                fnlisp  = fn(datalisp;  periodic = true, filter = U.ConvKernel(7))[D.PlaneXY()]
                fnjulia = fn(datajulia; periodic = true, filter = U.ConvKernel(7))[D.PlaneXY()]
                err = @. abs(fnlisp - fnjulia) / fnlisp
                npzwrite("result-rounded/$(fn)-$(s)-$(side).npy", err)
            end
        end
    end
end

function bar!()
    map(sides) do side
        datalisp  = load("julia/data-0-$(side).tga") .|> Gray |> BitArray
        U.lowfreq_energy_ratio(datalisp)
    end
end

function baz!()
    for side in sides
        perjl = map(1:9) do s
            data = load("julia-lin/data-$(s)-$(side).tga") .|> Gray .|> Float64 .|> round
            sum(U.extract_edges(data, U.ConvKernel(7), U.Torus()))
        end

        perlisp = map(1:9) do s
            data = load("lisp/data-$(s)-$(side).tga") .|> Gray .|> Float64
            sum(U.extract_edges(data, U.ConvKernel(7), U.Torus()))
        end

        npzwrite("per/$(side).npy", hcat(perjl, perlisp))
    end
end

end
