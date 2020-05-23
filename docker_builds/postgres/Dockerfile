FROM postgres:12
COPY --chown=postgres:postgres postgres.conf /etc/postgres.conf
RUN echo -e '#!bin/sh \ncreatedb -O postgres ${POSTGRES_DB}\n echo "Created DB ${POSTGRES_DB}"' > /docker-entrypoint-initdb.d/99_create_db.sh \
    && chmod 755 /docker-entrypoint-initdb.d/99_create_db.sh