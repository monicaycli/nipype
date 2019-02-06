NEURODOCKER_IMAGE="kaczmarj/neurodocker:0.4.3"
NIPYPE_BASE_IMAGE="nipype/nipype:base"
PKG_MANAGER="apt"

docker run --rm "$NEURODOCKER_IMAGE" generate docker \
  --base "$NIPYPE_BASE_IMAGE" --pkg-manager "$PKG_MANAGER" \
  --user neuro \
  --miniconda create_env=neuro \
              conda_install='python=3.6
                             icu=58.1 libxml2 libxslt matplotlib mkl numpy paramiko
                             pandas psutil scikit-learn scipy traits=4.6.0' \
              pip_install="grabbit==0.1.2 https://github.com/INCF/pybids/tarball/0.6.5" \
              activate=true \
  --copy docker/files/run_builddocs.sh docker/files/run_examples.sh \
         docker/files/run_pytests.sh nipype/external/fsl_imglob.py /usr/bin/ \
  --copy . /src/nipype \
  --user root \
  --run 'chown -R neuro /src
&& chmod +x /usr/bin/fsl_imglob.py /usr/bin/run_*.sh
&& . /etc/fsl/fsl.sh
&& ln -sf /usr/bin/fsl_imglob.py ${FSLDIR}/bin/imglob
&& mkdir /work
&& chown neuro /work' \
  --user neuro \
  --miniconda use_env=neuro \
              pip_opts="-e" \
              pip_install="/src/nipype[all]" \
  --user root \
  --install connectome-workbench \
  -r 'cp /neurodocker/startup.sh /singularity' \
  -r 'mkdir /scratch && mkdir /apps && mkdir /apps2' \
  --user neuro \
  --workdir /work

