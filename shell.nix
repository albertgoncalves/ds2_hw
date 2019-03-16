{ pkgs ? import <nixpkgs> {} }:
with pkgs; mkShell {
    name = "Python";
    buildInputs = [ (python36.withPackages(ps: with ps;
                        [ pip
                          csvkit
                          matplotlib
                          descartes
                        ]
                    ))
                  ];
    shellHook = ''
        directory="deps/"
        requirements="requirements.txt"
        if [ ! -d $directory ]; then
            pip install -t $directory -r $requirements
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
        fi
    '';
}
