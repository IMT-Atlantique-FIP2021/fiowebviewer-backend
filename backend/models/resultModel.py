from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from models.resultsListModel import ShortenResult, ShortenJob


class UploadID(BaseModel):
    id: str


class JobOptions(BaseModel):
    name: str
    numjobs: Optional[str]
    ioengine: Optional[str]
    direct: str
    invalidate: Optional[str]
    size: str
    rw: str
    rwmixread: Optional[str]
    randrepeat: Optional[str]
    bs: Optional[str]
    bssplit: Optional[str]
    iodepth: str
    runtime: str


class SlatNs(BaseModel):
    min: int
    max: int
    mean: float
    stddev: float


class Percentile(BaseModel):
    class Config:
        allow_population_by_field_name = True

    field_1_000000: int = Field(alias="1.000000")
    field_5_000000: int = Field(alias="5.000000")
    field_10_000000: int = Field(alias="10.000000")
    field_20_000000: int = Field(alias="20.000000")
    field_30_000000: int = Field(alias="30.000000")
    field_40_000000: int = Field(alias="40.000000")
    field_50_000000: int = Field(alias="50.000000")
    field_60_000000: int = Field(alias="60.000000")
    field_70_000000: int = Field(alias="70.000000")
    field_80_000000: int = Field(alias="80.000000")
    field_90_000000: int = Field(alias="90.000000")
    field_95_000000: int = Field(alias="95.000000")
    field_99_000000: int = Field(alias="99.000000")
    field_99_500000: int = Field(alias="99.500000")
    field_99_900000: int = Field(alias="99.900000")
    field_99_950000: int = Field(alias="99.950000")
    field_99_990000: int = Field(alias="99.990000")


class ClatNs(BaseModel):
    min: int
    max: int
    mean: float
    stddev: float
    percentile: Percentile


class LatNs(BaseModel):
    min: int
    max: int
    mean: float
    stddev: float


class ReadWrite(BaseModel):
    io_bytes: int
    io_kbytes: int
    bw_bytes: int
    bw: int
    iops: float
    runtime: int
    total_ios: int
    short_ios: int
    drop_ios: int
    slat_ns: SlatNs
    clat_ns: ClatNs
    lat_ns: LatNs
    bw_min: int
    bw_max: int
    bw_agg: float
    bw_mean: float
    bw_dev: float
    bw_samples: int
    iops_min: int
    iops_max: int
    iops_mean: float
    iops_stddev: float
    iops_samples: int


class Trim(BaseModel):
    class Config:
        extra = Extra.allow

    io_bytes: int
    io_kbytes: int
    bw_bytes: int
    bw: int
    iops: float
    runtime: int
    total_ios: int
    short_ios: int
    drop_ios: int
    slat_ns: SlatNs
    clat_ns: ClatNs
    lat_ns: LatNs
    bw_min: int
    bw_max: int
    bw_agg: float
    bw_mean: float
    bw_dev: float
    bw_samples: int
    iops_min: int
    iops_max: int
    iops_mean: float
    iops_stddev: float
    iops_samples: int


class Sync(BaseModel):
    lat_ns: LatNs
    total_ios: int


class IodepthLevel(BaseModel):
    class Config:
        allow_population_by_field_name = True

    field_1: float = Field(alias="1")
    field_2: float = Field(alias="2")
    field_4: float = Field(alias="4")
    field_8: float = Field(alias="8")
    field_16: float = Field(alias="16")
    field_32: float = Field(alias="32")
    field_gte_64: float = Field(alias=">=64")


class IodepthSubmitOrComplete(BaseModel):
    class Config:
        allow_population_by_field_name = True

    field_0: float = Field(alias="0")
    field_4: float = Field(alias="4")
    field_8: float = Field(alias="8")
    field_16: float = Field(alias="16")
    field_32: float = Field(alias="32")
    field_64: float = Field(alias="64")
    field_gte_64: float = Field(alias=">=64")


class LatencyNsUs(BaseModel):
    class Config:
        allow_population_by_field_name = True

    field_2: float = Field(alias="2")
    field_4: float = Field(alias="4")
    field_10: float = Field(alias="10")
    field_20: float = Field(alias="20")
    field_50: float = Field(alias="50")
    field_100: float = Field(alias="100")
    field_250: float = Field(alias="250")
    field_500: float = Field(alias="500")
    field_750: float = Field(alias="750")
    field_1000: float = Field(alias="1000")


class LatencyMs(BaseModel):
    class Config:
        allow_population_by_field_name = True

    field_2: float = Field(alias="2")
    field_4: float = Field(alias="4")
    field_10: float = Field(alias="10")
    field_20: float = Field(alias="20")
    field_50: float = Field(alias="50")
    field_100: float = Field(alias="100")
    field_250: float = Field(alias="250")
    field_500: float = Field(alias="500")
    field_750: float = Field(alias="750")
    field_1000: float = Field(alias="1000")
    field_2000: float = Field(alias="2000")
    field_gte_2000: float = Field(alias=">=2000")


class Job(BaseModel):
    class Config:
        allow_population_by_field_name = True

    jobname: str
    groupid: int
    error: int
    eta: int
    elapsed: int
    job_options: JobOptions = Field(alias="job options")
    read: ReadWrite
    write: ReadWrite
    trim: Trim
    sync: Sync
    job_runtime: int
    usr_cpu: float
    sys_cpu: float
    ctx: int
    majf: int
    minf: int
    iodepth_level: IodepthLevel
    iodepth_submit: Optional[IodepthSubmitOrComplete]
    iodepth_complete: Optional[IodepthSubmitOrComplete]
    latency_ns: LatencyNsUs
    latency_us: LatencyNsUs
    latency_ms: LatencyMs
    latency_depth: int
    latency_target: int
    latency_percentile: float
    latency_window: int


class DiskUtilItem(BaseModel):
    name: str
    read_ios: int
    write_ios: int
    read_merges: int
    write_merges: int
    read_ticks: int
    write_ticks: int
    in_queue: int
    util: float


class FioResult(BaseModel):
    class Config:
        allow_population_by_field_name = True

    result_id: Optional[str] = Field(alias="id")
    name: Optional[str] = None
    tags: Optional[List[str]] = None
    timestamp: int
    timestamp_ms: int
    time: str
    fio_version: str = Field(alias="fio version")
    jobs: List[Job]
    disk_util: List[DiskUtilItem]

    def shortened(self) -> ShortenResult:
        """
        Shorten a FioResult

        :return: ShortenResult
        """
        jobs_list = []
        for current_job in self.jobs:
            jobs_list.append(
                ShortenJob(
                    jobname=current_job.jobname,
                    error=current_job.error,
                )
            )
        return ShortenResult(
            id=self.result_id,
            name=self.name,
            tags=self.tags,
            time=self.time,
            timestamp=self.timestamp,
            jobs=jobs_list,
        )
