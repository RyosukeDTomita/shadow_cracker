FROM python:3.12.4-slim-bullseye
WORKDIR /app

ARG VERSION="0.1.0"
# FIXME: hogehoge
LABEL version="${VERSION}" \
      author="RyosukeDTomita" \
      docker_build="docker buildx build . -t shadow_cracker" \
      docker_run="docker run shadow_cracker" \
      docker_compose_build="docker buildx bake" \
      docker_compose_run="docker compose run shadow_cracker_app"


ARG USER_NAME="sigma"

# install library
RUN <<EOF bash -ex
python3 -m pip install --upgrade pip setuptools wheel --no-cache-dir
python3 -m pip install requests
rm -rf /var/lib/lists
EOF

# create execution user with sudo
RUN <<EOF bash -ex
echo 'Creating ${USER_NAME} group.'
addgroup ${USER_NAME}
echo 'Creating ${USER_NAME} user.'
adduser --ingroup ${USER_NAME} --gecos "sigma_super_app user" --shell /bin/bash --no-create-home --disabled-password ${USER_NAME}
EOF

COPY --chown=${USER_NAME}:${USER_NAME} ./shadow_cracker.py /app/shadow_cracker.py

USER ${USER_NAME}
CMD ["python3", "-u", "/app/shadow_cracker.py"]

