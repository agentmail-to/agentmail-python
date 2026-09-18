{
  description = "agentmail - Python SDK";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.11";
    flake-utils.url = "github:numtide/flake-utils";
    flake-compat.url = "github:edolstra/flake-compat";
    flake-compat.flake = false;
  };

  outputs = { self, nixpkgs, flake-utils, flake-compat, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        python = pkgs.python3;

        agentmail = python.pkgs.buildPythonPackage {
          pname = "agentmail";
          version = "0.2.10";
          format = "pyproject";
          src = ./.;

          nativeBuildInputs = [
            python.pkgs.poetry-core
          ];

          propagatedBuildInputs = with python.pkgs; [
            httpx
            pydantic
            pydantic-core
            typing-extensions
            websockets
          ];

          pythonImportsCheck = [ "agentmail" ];

          # Tests require network access / API keys
          doCheck = false;
        };
      in
      {
        packages.default = agentmail;

        devShells.default = pkgs.mkShell {
          packages = [
            (python.withPackages (ps: [
              agentmail
              ps.pytest
              ps.pytest-asyncio
              ps.pytest-xdist
              ps.python-dateutil
              ps.mypy
              ps.ruff
            ]))
          ];
        };
      }
    ) // {
      overlays.default = final: prev: {
        pythonPackagesExtensions = (prev.pythonPackagesExtensions or []) ++ [
          (python-final: python-prev: {
            agentmail = python-final.buildPythonPackage {
              pname = "agentmail";
              version = "0.2.10";
              format = "pyproject";
              src = self;

              nativeBuildInputs = [
                python-final.poetry-core
              ];

              propagatedBuildInputs = with python-final; [
                httpx
                pydantic
                pydantic-core
                typing-extensions
                websockets
              ];

              pythonImportsCheck = [ "agentmail" ];
              doCheck = false;
            };
          })
        ];
      };
    };
}
