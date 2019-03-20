{ pkgs ? import <nixpkgs> {} }:
with pkgs; mkShell {
    name = "Python";
    buildInputs = [
        (python36.withPackages(ps: with ps; [
            pip
            pandas
            numpy
            matplotlib
            flake8
            shapely     # | on linux, shapely fails via pip
            fiona       # | hence 'pip install --no-deps'...
            six         # | all geopandas deps included here
            pyproj      # | http://geopandas.org/install.html
            descartes   # |
        ]))
        (with rPackages; [
            R
        ])
        glibcLocales
        gdal
        jq
        sqlite
        rlwrap
    ] ++ (with python36Packages; [
        (csvkit.overridePythonAttrs (oldAttrs: {checkPhase = "true";}))
    ]);
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
        . .alias
        export WD=$(pwd)
    '';
}
