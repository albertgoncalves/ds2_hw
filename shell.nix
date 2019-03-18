{ pkgs ? import <nixpkgs> {} }:
with pkgs; mkShell {
    name = "Python";
    buildInputs = [ (python36.withPackages(ps: with ps;
                        [ pip
                          pandas
                          numpy
                          matplotlib
                          csvkit
                          flake8
                          shapely       # | on linux, shapely fails via pip
                          fiona         # | hence 'pip install --no-deps'...
                          six           # | all geopandas deps included here
                          pyproj        # | http://geopandas.org/install.html
                          rtree         # |
                          descartes     # |
                          pysal         # |
                        ]
                    ))
                    gdal
                    jq
                  ];
    shellHook = ''
        directory="src/deps/"
        requirements="requirements.txt"
        if [ ! -d $directory ]; then
            pip install --no-deps -t $directory -r $requirements
        fi
        export PYTHONPATH=$directory
        for subdir in data pngs; do
            if [ ! -d $subdir ]; then
                mkdir $subdir
            fi
        done
        if [ $(uname -s) = "Darwin" ]; then
            alias ls='ls --color=auto'
            alias ll='ls -al'
        else
            alias open="xdg-open"
        fi
        . .alias
    '';
}
